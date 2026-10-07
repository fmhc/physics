# DIM-LEITER-QBALL-1: Bis zu welcher Dimension bleibt der Q-Ball aus Papier I stabil, und wie waechst seine Mindestladung? (Runde 42)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 18:46:54 CEST (date), vor jeder
  Rechnung.
- **Finn (04.10.), woertlich:**
  - Zwischen 18:33 und 18:36: "untersuche ob wir eine zusammengesetzte formel ableiten können für irgendwas - eine länge
    oder so, eine konstante oder ein gleichbleibendes verhältnis oder sowas, was in einem größeren system sinn ergibt -
    aus einem term für 1-dimensionalität, einem term für 2-dimensionalität und 3-dimensionalität und
    4-dimensionalität und dann n-dimensionalitäten und ggf. sogar 12+n dimensionalitäten, ... klingen wellen von 2d
    auf 3d bzw nd n+1d ab und bis wann bleibt was stabil?"
  - Zwischen 18:36 und 18:40: "... können wir von einem einpendeln zwischen 3-4 dimensionen oder so die stabil sind
    ausgehen? vllt 12 die partiell existieren können, und mehr nur super kurzlebig?"
- **Modell:** Papier I, U(S) = S - S^2 + S^3/2 mit S = |phi|^2, Masse m = 1; radialer Q-Ball phi = f(r) e^{i omega t} in
  D Raumdimensionen: f'' + (D-1)/r f' + omega^2 f - U'(f^2) f = 0.
- **Regel Dimensionsvergleich (AGENTS.md):** Hier ist die Raumdimension die Stellgroesse. Ein radialer Lauf ist kein
  voller Stabilitaetsnachweis; das Kriterium hier ist Vakhitov-Kolokolov (VK) plus E < m Q.
- Kennzeichen: [M] Mathematik, [E] Rechnung, [L] Literatur, [P] Projektdatei, [H] Hypothese.

## Ableitbarkeitsprobe (Leitung)

**Vorab ableitbar [M]:**
- Existenzfenster omega in (omega_min, 1) mit omega_min^2 = min U(S)/S = 1/2, also omega_min = 0,7071, in jeder
  Dimension.
- Dicke Wand (omega -> 1, kubisch-NLS-artig): Q ~ eps^(2-D) mit eps^2 = 1 - omega^2. Fuer D = 1 geht Q gegen 0, fuer
  D = 2 gegen einen festen Wert, fuer D >= 3 gegen unendlich; dort ist der Ast nach VK instabil.
- Duenne Wand (omega -> omega_min): Q -> unendlich, VK-stabil, in jeder Dimension [L].
- Fuer D >= 3 hat Q(omega) deshalb ein Minimum Q_min(D) (Wendepunkt), stabil auf der Seite der duennen Wand.

**Nicht ableitbar:**
- Die Zahlen omega_c(D), Q_min(D), die Schwelle E = m Q und der Verlauf ueber D = 1 bis 12.
- Der Verlauf in D = 2 (Vorzeichen von dQ/domega nahe 1 haengt am Quintik-Glied).
- Ob Q_min(D) einem einfachen Gesetz folgt ("zusammengesetzte Formel").

**Vorher:**
- Projekt-grep und Codex-Pfade pruefen (model-lab/papers/qball-bic-ladder-20260930/,
  coordination/resonance-20260930/). Liegt die D-Leiter schon vor, zitieren statt rechnen.
- An Codex ist die Frage per Bus gestellt (18:43).

## Messgroessen

- Je D = 1 bis 12:
  - Q(omega) und E(omega) auf einem Gitter in (omega_min, 1)
  - omega_c(D) und Q_min(D)
  - omega_s(D) (E = m Q)
- Stabilitaetsmass W(D): Anteil des Existenzfensters, der zugleich VK-stabil ist und E < m Q erfuellt.
- Kontrollen:
  - Schuss-Genauigkeit
  - Vergleich mit den 3D-Werten des Projekts (QB-BS-2D bzw. Papier I, per grep)
  - Dicke-Wand-Exponent 2 - D in D = 1, 3, 4

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| DQ0 | Kontrollen: Existenzgrenze 0,7071; Exponent 2 - D in D = 1, 3, 4 auf 10 %; 3D-Werte des Projekts auf 1e-3 | 85 % |
| DQ1 | [H] Fuer D = 3 bis 12 existiert der Wendepunkt (ableitbar), und Q_min(D) waechst streng monoton mit D | 70 % |
| DQ2 | [H] ln Q_min(D) ist linear in D auf 15 % fuer D = 3 bis 12 (exponentielles Wachstum) | 35 % |
| DQ3 | [H, Finns Einpendeln] Das Stabilitaetsmass W(D) ist bei D = 3 oder 4 am groessten | 10 % |

**Bedeutung (vorab):**
- **DQ3 trifft ein:** Unser Materieklumpen ist in 3 bis 4 Dimensionen am robustesten; das waere ein Baustein fuer Finns
  Einpendeln [H].
- **DQ3 verfehlt (erwartet):** Der Q-Ball ist in niedriger Dimension am robustesten, und mit jeder Dimension braucht er
  mehr Ladung. Hoehere Dimensionen sind dann nur fuer sehr grosse Klumpen stabil.
- **DQ2 trifft ein:** Die Mindestladung folgt einem einfachen Gesetz ueber D, eine zusammengesetzte Formel [H].

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu11 und cpu4. Je Lauf <= 10 min, 1 Thread. Zeitbox 90 min.
