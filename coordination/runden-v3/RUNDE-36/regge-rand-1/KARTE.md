# REGGE-RAND-1: Gibt ein Tetraedernetz, dessen Kantenlaengen eine Masse verbiegt, ein 1/r-Feld, und reicht der Rand? (Runde 36)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 23:02:41 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn ~22:30: "Wie kommen wir auf die spin2 kopplung ... aus punkten strichen Dreiecken ...? Reicht das als Schwerefeld
    was sich aus den gesamtklumpen- Rändern bildet?"
  - Dossier GRAVITON-NETZ-L (RUNDE-35/graviton-netz-l/DOSSIER.md, Abschnitt 6, RT-1): Spin 2 kommt aus Strichen, wenn
    sie Laengen sind (Regge).
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [S] an der Quelle gelesen (laut Dossier), [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Regge** [S, Dossier]: In 3D sitzt die Kruemmung als Fehlwinkel eps_e an den Kanten, und int R sqrt(g) dV =
  2 sum_e l_e eps_e.
- **Zeitsymmetrische Anfangsdaten** [L]: Die Hamilton-Bedingung lautet R^(3) = 16 pi G rho.
  - Verteilt man jede Kante halb auf ihre zwei Ecken, wird daraus die Eckenregel sum_{e an v} l_e eps_e = 16 pi G m_v.
  - Die Normierung ist vor dem Lauf zu pruefen.
- **Konformer Ansatz:** l_e = l_e^0 psi_e^2 (psi am Kantenmittelpunkt, z. B. Mittel der zwei Ecken), psi = 1 + delta psi.
  - Im Kontinuum gilt linear: Laplace delta psi = -2 pi G rho, also delta psi = G M/(2 r) (isotrope Schwarzschild-Form)
    [L].
- **Was neu ist** (Dossier: vorab ableitbar ist nur der Kontinuumsausgang): ob die Fehlwinkel-Eckenregel auf dem
  Tetraedergitter einen positiven, richtungsfreien diskreten Laplace-Operator ergibt, ohne Schachbrett-Nullmoden (vgl. die
  fuenfte Nullmode bei Rocek/Williams [S, sekundaer]), und wie stark die Kuhn-Diagonalen die Richtungsfreiheit stoeren.
- **"Raender"** [M]: Die Gauss-Masse M(R) = -(1/(2 pi G)) (Flaechenintegral von grad delta psi) auf einer Kugel um die
  Quelle zaehlt nur die eingeschlossene Gesamtquelle. Ein kompakter und ein ausgedehnter Klumpen gleicher Gesamtquelle
  geben aussen dieselbe Randmasse.
- **Erweiterung (nichtlinear, wahlweise)** [L: Brill-Lindquist]: Bei zwei Quellen im Abstand d ist die Randmasse
  m1 + m2 - G m1 m2/d. Die Bindungsenergie, also die Anziehung, erscheint als Randgroesse.

## Test (Code-Agent)

- **Gitter:** Tetraedergitter aus der Kuhn- bzw. Freudenthal-Zerlegung des kubischen Gitters (6 Tetraeder je Wuerfel),
  L = 32 und 64. Gegenprobe Tetraeder-Oktaeder-Wabe, falls die Zeit reicht.
- **Fehlwinkel:** aus exakten Diederwinkeln je Kante (2 pi - Summe der Diederwinkel der Tetraeder um die Kante).
  - Pruefen, dass das ungestoerte Gitter flach ist.
- **Linearisierung:** Jacobi-Matrix d eps/d psi numerisch oder analytisch. Daraus der Eckenoperator A delta psi = 16 pi G m.
  - Dazu Spektrum bzw. Nullraum von A auf einem kleinen Gitter (L = 8 bis 12).
- **Quellen:**
  - (a) Punktquelle an einer Ecke
  - (b) ausgedehnter Klumpen (Kugel vom Radius 6, gleiche Gesamtquelle)
- **Rand:** periodisch mit Hintergrundkorrektur, oder Dirichlet delta psi = 0 am Rand eines grossen Wuerfels; offenlegen.
- **Gemessen:**
  - r delta psi(r) entlang mehrerer Richtungen
  - Richtungsschwankung bei festem r
  - Gauss-Masse auf konzentrischen Wuerfel- bzw. Kugelflaechen fuer (a) und (b)
- **Wahlweise:** nichtlineare Loesung fuer zwei Quellen und Randmasse gegen Brill-Lindquist.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| RR0 | Kontrolle: ungestoertes Kuhn-Gitter flach (alle Fehlwinkel < 1e-12); Eckenoperator symmetrisch; gleichmaessige Skalierung von psi ist Nullmode | 90 % |
| RR1 | Der Eckenoperator ist auf dem Unterraum ohne Konstante positiv definit, ohne weitere Nullmoden (keine Schachbrettmoden) | 65 % |
| RR2 | Punktquelle (L = 64): r delta psi(r) = G M/2 innerhalb 3 % fuer 6 <= r <= L/4 (nach Rand- bzw. Hintergrundkorrektur) | 70 % |
| RR3 | Richtungsschwankung von delta psi bei r = 12 unter 2 % | 60 % |
| RR4 | Kompakter und ausgedehnter Klumpen gleicher Gesamtquelle geben auf Raendern mit R >= 10 dieselbe Gauss-Masse innerhalb 1 % | 75 % |
| RR5 | Wahlweise, nichtlinear: Randmasse - (m1 + m2) = -G m1 m2/d innerhalb 20 % fuer m/d <= 0,1 | 40 % |

**Bedeutung (vorab):**
- RR1 bis RR4 treffen ein: In Finns Bild mit Strichen als Laengen gibt eine Masse ueber die Fehlwinkel der Tetraeder ein
  1/r-Feld. Der Rand eines Klumpens zaehlt genau die eingeschlossene Gesamtquelle, egal wie sie innen verteilt ist.
  - Das ist der Spin-2-Weg (Regge); er ist hineingesteckt, nicht hergeleitet (Dossier, Regime A).
- RR5 trifft ein: Die Anziehung zweier Massen erscheint als Bindungsenergie am Rand ("Anziehung aus dem Rand").
- RR1 verfehlt: Die Eckenregel hat Schachbrett-Nullmoden. Dann braucht Finns Tetraedernetz eine andere Zuordnung der
  Kruemmung; beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a (CPU- oder GPU-Skript; nicht cpu, cpu2, cpu3,
  cpu4, cpu5, cpu6, p4000b); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
