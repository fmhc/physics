# DIM-BEUTEL Plan-Nachtrag 1 (NACHTRAEGLICH zum eingefrorenen Plan, aber VOR jedem .69-Lauf)

- Geschrieben ab 2026-10-02 10:02:13 CEST (date), nach dem Einfrieren von PLAN.md (09:59:01) und vor jeder
  Syntaxpruefung, jedem Rauchtest und jedem Lauf. Es gibt noch keine Zahlen.
- Er aendert nichts an Modell, Graphen, Q-Gitter, D1 bis D5, Wertungswerten und Bedeutung.
- Anlass: Beim Schreiben des Codes fielen zwei unscharfe Definitionen im Plan auf.

## N1: Randbereich der Gitter (ersetzt "D_out ... bei Gittern" aus PLAN 3)

- Fehler im Plan: Auf den Gittern ist der Graphabstand die L1-Metrik. "Graphabstand >= Randabstand - 2" haette auch
  innere Knoten auf den Diagonalen erfasst. Im 64^3-Gitter laegen solche Knoten nur ~17 euklidisch vom Zentrum, also
  im Beutel.
- Neu: Der Randbereich der Gitter G1 bis G3 sind die Knoten mit mindestens einer Koordinate <= 1 oder >= L - 2, also
  die zwei aeussersten Lagen.
- Sierpinski bleibt wie geplant: Graphabstand >= H vom Startknoten (Ferngebiet).
- Die Gueltigkeitsschwellen bleiben: max phi(Rand) <= 1e-6 x max phi und max |1 - chi(Rand)| <= 1e-6.

## N2: Konvergenz eines Punktes (praezisiert "Gradient <= 10 x gtol" aus PLAN 4)

- Der Loeser arbeitet mit Jacobi-skalierten Variablen x = s y. Seine Toleranz gtol gilt deshalb fuer den skalierten,
  projizierten Gradienten s * dE/dx.
- Neu: Ein Punkt ist konvergiert, wenn der skalierte projizierte Gradient <= 100 x gtol ist UND der
  Identitaetsrest |E - omega Q - E_chi|/E <= 1e-6.
- Begruendung: Gilt die Identitaet (Amplitudenrichtung stationaer), ist omega in Formfehlern von zweiter Ordnung
  genau (Rayleigh-Quotient). Der unskalierte Gradient wird mitberichtet.
- Ohne Skalierung (falls der Rauchtest das nahelegt) ist s = 1, und die Regel gilt unveraendert.

## N3: Zeitgrenze je Aufruf

- Ueberschreitet ein Aufruf 540 s, endet die Minimierung des laufenden Punkts mit dem bis dahin besten Zustand. Der
  Punkt wird als "ZEITGRENZE" markiert und ist nicht gueltig. Der naechste Aufruf setzt an diesem Zustand fort und
  rechnet den Punkt neu.
