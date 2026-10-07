# KREIN-1: Krein-Signatur der stillen Moden (Plan, Herleitung, Erwartung vorab)

- Auftrag: Leitung claude-primary, 2026-09-30 10:13:41 CEST (Finn: "mach das"). Offen seit Runde 6 (L4-BIC-LITERATUR.md, N7).
- Autor: Claude (Beweis-Agent aus BEWEIS-1). Plan geschrieben ab 2026-09-30 10:20:28 CEST (date), **bevor** irgendeine
  Signatur numerisch ausgerechnet wurde.

## 1. Herleitung (Schreibtisch)

Konvention wie im Auftrag: phi = e^{i omega t} (f + psi), psi = a e^{i rho t} + b e^{-i rho t}, a und b reell, Kanal a mit
Laborfrequenz omega + rho (offen), Kanal b mit omega - rho (geschlossen, fuer rho > omega negative Laborfrequenz).

**Erhaltene quadratische Form.** Im mitrotierenden Rahmen ist die Linearisierung autonom und Hamiltonsch. Ihre
Hamiltonfunktion ist die zweite Variation des Lyapunov-Funktionals H - omega Q. Mit H = int |phi_t|^2 + |grad phi|^2 +
U(|phi|^2) und Q = 2 Im int phi* phi_t (Q-Ball: Q = 2 omega int f^2) gilt in den Variablen Phi = e^{-i omega t} phi,
Pi = e^{-i omega t} phi_t:

- H - omega Q = int |Pi - i omega Phi|^2 + |grad Phi|^2 + U(|Phi|^2) - omega^2 |Phi|^2.
- Also am Q-Ball (Pi = i omega f):
  E_2 = int |psi_t|^2 + |grad psi|^2 + (dp - omega^2) |psi|^2 + sp Re(psi^2) d^3x,
  mit dp = U' + U'' S = 1 - 4S + 9/2 S^2 und sp = U'' S = -2S + 3S^2.
- Probe: E_2 ist auch die Noether-Energie der quadratischen Lagrangefunktion
  L_2 = |psi_t + i omega psi|^2 - |grad psi|^2 - U'|psi|^2 - (1/2) U'' S (psi + psi*)^2
  (gerechnet; ihre Euler-Lagrange-Gleichung ist die Linearisierung des BRIEF von BEWEIS-1).

**Wert auf der Mode.** Einsetzen von psi = a e^{i rho t} + b e^{-i rho t}:
- Der konstante Teil ist int rho^2 (a^2 + b^2) + |grad a|^2 + |grad b|^2 + (dp - omega^2)(a^2 + b^2) + 2 sp a b.
- Der Teil mit cos(2 rho t) verschwindet wegen der Modengleichungen (gerechnet).
- Mit den Modengleichungen (mal a bzw. b, integriert, addiert:
  int |grad a|^2 + |grad b|^2 + dp (a^2 + b^2) + 2 sp a b = int (omega + rho)^2 a^2 + (omega - rho)^2 b^2):

  **E_2 = 2 rho int [(omega + rho) a^2 + (rho - omega) b^2] d^3x = 2 rho N**, zeitlich konstant.

Die Krein-Signatur einer Mode ist das Vorzeichen von E_2 auf ihrem reellen invarianten Unterraum. Bei rho > 0 ist sie
das Vorzeichen der symplektischen Norm N = int (omega + rho) a^2 - (omega - rho) b^2.

- **Vorzeichen gegen den Vorschlag im Auftrag:** Die Vermutung "(omega + rho)||a||^2 + (omega - rho)||b||^2" ist die
  Ladung der Stoerung (Q_2), nicht die Krein-Norm. Der b-Term geht mit (rho - omega) ein, nicht mit (omega - rho).
- Probe am freien Feld (S = 0, exakt): H_2 = 2 int (omega+rho)^2 a^2 + (omega-rho)^2 b^2 und
  Q_2 = 2 int (omega+rho) a^2 + (omega-rho) b^2. Daraus H_2 - omega Q_2 = 2 rho [(omega+rho) a^2 + (rho-omega) b^2], dasselbe.
- **bic2.py:** Es normiert anders; U, V gehoeren dort zu e^{-i omega t}, Kanal U mit omega + rho.
  - Seine "Krein-Norm" N_K = int_0^R (omega + Re rho)|U|^2 - (omega - Re rho)|V|^2 dr (PLAN.md Runde 7, Punkt 50)
    ist dieselbe Form in reduzierten Funktionen (U = r u).
  - Normierung dort: n_b = 1, d. h. Ursprungskoeffizient des geschlossenen Kanals V ~ r^(l+1) gleich 1.
  - bic2 vermerkte bereits: "Fuer rho > omega sind beide Terme von N_K positiv."
  - Die vorliegende Herleitung ueber H - omega Q ist davon unabhaengig.
- Allgemeiner (gleiche Rechnung): Fuer jede Stoerkomponente mit Zeitfaktor e^{-i omega t} und reellen
  Kopplungen dp, sp gilt dieselbe Formel. Das umfasst den gemischten Ball, psi_2-Kanal (gfbic.py: dp = U',
  sp = -g J S).

**Folgerung (strukturell):** Fuer rho > omega > 0 sind beide Gewichte positiv (omega + rho > 0, rho - omega > 0). Jede
nichttriviale Mode hat dann E_2 > 0, also positive Krein-Signatur, unabhaengig von der Eigenfunktion. Negative Energie
ist nur fuer 0 < rho < omega moeglich, und nur wenn der b-Anteil ueberwiegt.

**Gegenprobe (unabhaengig, Auftrag Schritt 2):** E_2 direkt bei t = 0 aus Feld und Zeitableitung:
psi(0) = a + b, psi_t(0) = i rho (a - b), also
E_2(0) = int rho^2 (a - b)^2 + |grad(a + b)|^2 + (dp + sp - omega^2)(a + b)^2 d^3x.
Diese Groesse benutzt Ableitungen und Potential, nicht die Gewichte. Die Gleichheit E_2(0) = 2 rho N gilt nur, wenn
(a, b) die Modengleichungen erfuellt. Sie prueft also Formel und Eigenfunktion zugleich.

Reduziert (a = A/r Y_lm, b = B/r Y_lm, Y_lm reell normiert, A(0) = B(0) = 0), je Einheit Winkelnorm:
- N = int_0^R (omega + rho) A^2 + (rho - omega) B^2 dr,
- E_2(0) = int_0^R rho^2 (A - B)^2 + (A' + B')^2 + l(l+1)(A + B)^2/r^2 + (dp + sp - omega^2)(A + B)^2 dr.

## 2. Erwartung je Stelle (vorab, vor jeder Rechnung)

Werte omega*^2 und rho* aus RUNDE-07.md, RUNDE-08/sp1/ERGEBNIS.md, RUNDE-09/MODELL-DUENNWAND.md,
RUNDE-08/gf-bic/ERGEBNIS.md:

| Stelle | omega*^2 | rho* | omega* | rho* - omega* | Erwartung Signatur | Erwartung Gegenprobe |
|---|---|---|---|---|---|---|
| l = 0, n = 1 | 0,797677 | 1,744618 | 0,8931 | 0,851 | positiv (strukturell) | E_2(0)/(2 rho N) = 1 bis 1e-5 |
| l = 0, n = 2 | 0,685129 | 1,690357 | 0,8277 | 0,863 | positiv | ebenso |
| l = 0, n = 3 | 0,631449 | 1,652588 | 0,7946 | 0,858 | positiv | ebenso |
| l = 1, n = 1 | 0,754496 | 1,826342 | 0,8686 | 0,958 | positiv | ebenso |
| l = 1, n = 2 | 0,660280 | 1,717301 | 0,8126 | 0,905 | positiv | ebenso |
| l = 2, n = 1 | 0,643905 | 1,762082 | 0,8024 | 0,960 | positiv | ebenso |
| l = 2, n = 2 | 0,606981 | 1,694040 | 0,7791 | 0,915 | positiv | ebenso |
| gemischter Ball Z1 (psi_2, g = 0,2) | 0,7113723 | 1,6888290 | 0,8434 | 0,845 | positiv | ebenso |

Weitere Erwartungen:
- N (bei fester Normierung) haengt nicht vom Abschneideradius ab, bei zwei L bis auf 1e-6 relativ, weil die Mode
  exponentiell abfaellt.
- Der b-Anteil (geschlossener Kanal) traegt den groessten Teil der Norm. Der a-Anteil ist klein, er ist die
  unterdrueckte Abstrahlung. Den Bruchteil schaetze ich auf 5 bis 30 Prozent; das ist unsicher.
- l = 1 und l = 2: Alle m-Komponenten haben dieselbe Radialfunktion und dasselbe rho, also gleiche Signatur. Eine
  U(2l+1)-Symmetrie der quadratischen Dynamik ist damit vertraeglich.

Was die Erwartung widerlegen wuerde:
- E_2(0) < 0 an einer Stelle.
- Eine Gegenprobe E_2(0)/(2 rho N) deutlich neben 1, dann ist die Formel falsch oder die Eigenfunktion keine Mode.
- N je nach L verschieden, dann ist die Mode nicht normierbar, also kein BIC an dieser Stelle.

## 3. Rechnung (Plan)

- Neues, von bic2 unabhaengiges float64-Programm krein.py (numpy/scipy, .69, Spur cpu5):
  - Profil per Schiessen mit Bisektion und linearem Schwanz.
  - Eigenfunktion aus zwei regulaeren Loesungen (Start r^(l+1)) und der Jost-Loesung (geschlossener Kanal
    e^{-kappa r} mal Hankel-Polynom, offener Kanal 0) mit Anschluss bei r_m (kleinste Quadrate; der Rest misst den
    Abstand zur Stelle).
  - Dann N, Anteile ||A||^2 und ||B||^2, E_2(0) und das Verhaeltnis.
  - Zwei Abschneideradien L = 36 und 44.
- Vergleich mit bic2 (unabhaengiger Code, torch, RK4): N_K aus lauf-69/aus-exakt-002 fuer l = 0, n = 1 bei gleicher
  Normierung (n_b = 1).
- Kontrollen:
  - Freies Feld analytisch (oben).
  - Nichtrelativistische Grenze: Fuer omega -> 1 und kleines rho wird N zu ||a||^2 - ||b||^2. Das ist die Form der
    NLS-Krein-Norm (Cuccagna, Pelinovsky, Vougalter 2005 [L?], an der Quelle zu pruefen).
- Streng (l = 0, n = 1):
  - Aus BEWEIS-1 sind rho* und omega* im zertifizierten Kasten, damit rho* - omega* >= 0,85 > 0.
  - Die Eigenfunktion ist nichttrivial, glatt und faellt exponentiell ab (Lemma J, R). Damit gilt die
    Formel E_2 = 2 rho N (partielle Integration zulaessig), und N > 0.
  - Eine numerische Huelle von N ist fuer das Vorzeichen nicht noetig. Der Wert selbst waere ein weiterer Schritt.
