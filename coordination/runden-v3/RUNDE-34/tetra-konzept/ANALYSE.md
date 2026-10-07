# Finns Tetraeder-Konzept mit Krafteinheiten: Analyse (Leitung, Runde 34)

- Leitung claude-primary, geschrieben ab 2026-10-03 19:03:46 CEST (date).
- Anlass: Finn ~19:00: "analysiere mal das konzept hier mit tetraeder und die weissen dinger sind krafteinheiten und die
  muessten eigentlich dadurch oder daran entlang fliessen".
- Quelle: ~/Downloads/Photos-1-001 (12).zip (18:59), kopiert und entpackt in diesen Ordner. Zwei Fotos vom 03.10.
  01:58:00 und 01:58:09 (8160 x 6120), Pruefsummen in BILDER.sha256; verkleinerte Fassungen *-klein.jpg.
- Kennzeichen: [B] am Bild abgelesen (kann ungenau sein), [E] eigene Projektrechnung, [M] Mathematik, [L] Literatur,
  [H] Hypothese.

## 1. Was die Fotos zeigen [B]

- **Sechs Knicklichter** auf dem Holztisch, als ebenes Bild eines Tetraeders: vier Ecken (oben, links, rechts, unten),
  sechs Kanten.
  - Aussen herum: oben-links (rot) und oben-rechts (blau), stark nach innen gebogen; unten-links (violett) und
    unten-rechts (hellblau), leicht nach innen gebogen.
  - Innen zwei Diagonalen, die sich kreuzen: waagerecht (violett, links-rechts, leicht gebogen) und senkrecht (orange,
    oben-unten, gerade).
  - Das ist genau der Blick auf ein Tetraeder entlang der Achse durch die Mitten zweier gegenueberliegender Kanten
    [M]. Diese zwei Kanten erscheinen als Diagonalen und kreuzen sich nur im Bild; im Raum gehen sie windschief
    aneinander vorbei.
  - Die nach innen gebogenen Staebe entsprechen unserem Knicklicht-Tetraeder aus TETRA-STAB (RUNDE-24).
- **18 weisse Filterstueckchen ("Krafteinheiten")**, alle an den Stabenden. Gezaehlt je Stab: an einem Ende 1, am
  anderen 2, also 3 je Stab, 6 x 3 = 18 [B].
- **Zwischen den Fotos** wandert eine Einheit entlang des orangen Stabs vom unteren zum oberen Ende. Die Summe bleibt 18
  [B]. Das passt zu "die fliessen daran entlang".

## 2. Was "Kraefte fliessen entlang der Staebe" physikalisch heissen kann

Es gibt zwei Lesarten mit verschiedenen Folgen.

### Lesart A: echte mechanische Kraefte (Zug und Druck in den Staeben)

- Im Ingenieurbau heisst das Kraftfluss [L]: Kraefte laufen als Zug oder Druck durch die Staebe, und an jedem Knoten
  heben sich die Kraefte vektoriell auf (Gleichgewicht).
- **Ein einzelnes Tetraeder hat keinen inneren Kraftkreislauf** [M, E]:
  - Als Gelenkwerk ist es genau bestimmt (3 * 4 - 6 = 6 Staebe), es hat also keine Eigenspannung.
  - Ohne Last von aussen fliesst nichts.
  - Unser Knicklicht-Tetraeder mit nach innen gebogenen Staeben (TETRA-STAB) traegt nur Eckmomente (Biegung), keine
    Laengskraefte [E].
  - Zieht man zwei Ecken auseinander, traegt nur der Stab dazwischen; die anderen fuenf bleiben kraftfrei [M].
- **Kraftkreislaeufe entstehen erst, wenn Tetraeder verspannt zusammengesetzt werden:**
  - fuenf Tetraeder um eine Kante (FRUST-3D, RUNDE-27): Achse auf Zug, Speichen auf Druck, Ring auf Zug, ein
    geschlossener Kreislauf [E]
  - der Ikosaeder (ICO-STAB, RUNDE-29) [E]
- **Gebogene Staebe und Kraftfluss** [M]: Laeuft eine Laengskraft T durch einen gekruemmten Stab (Kruemmung kappa),
  entsteht eine Querkraft T kappa je Laenge.
  - Zug zieht einen Bogen gerade, Druck biegt ihn weiter (bis zum Knicken).
  - Nach innen gebogene Staebe passen also zu Druck in diesen Staeben oder zu einer Vorbiegung.

### Lesart B: Einheiten, die erhalten bleiben und wandern (Fluss wie Strom)

- Bleibt die Zahl der Einheiten gleich und gilt an jeder Ecke "was hineinfliesst, fliesst hinaus", dann ist das das
  Kirchhoff-Gesetz [M].
- **Auf dem Kantengeruest des Tetraeders** (4 Ecken, 6 Kanten) gibt es genau 6 - 4 + 1 = 3 unabhaengige Kreislaeufe [M],
  zum Beispiel ums Dreieck dreier Flaechen; die vierte Flaeche ergibt sich daraus. Ein dauerhafter Fluss ohne Quelle ist
  also immer ein Wirbel um Flaechen.
- **Startet oder endet der Fluss an einer Ecke,** ist diese Ecke eine Quelle bzw. Senke. In einem grossen Netz aus
  Tetraedern verhalten sich solche Quellen wie Ladungen.
  - Bei erhaltenem Fluss mit Kosten proportional zum Quadrat des Flusses ziehen sie sich ueber grosse Entfernungen wie
    Coulomb an. Das ist die Gitterform des Elektromagnetismus [L].
- **Spin-Eis ist genau diese Lesart, nur "durch" statt "entlang":** Dort sitzen die Einheiten (Spins) auf den Ecken, die
  zwei Tetraeder teilen. Sie fliessen von Tetraedermitte zu Tetraedermitte, also durch die Tetraeder. Die Regel je
  Tetraeder lautet "so viel rein wie raus" [L]. Das prueft Test A (EIS-1) gerade.
- **Abzaehlen am Foto** [B, H, unsicher]:
  - Liest man "2 an einem Ende, 1 am anderen" als Richtung des Flusses, dann ist auf Foto 1 an jeder Ecke Zufluss und
    Abfluss nicht gleich: oben und links je eine Einheit zu wenig, rechts und unten je eine zu viel.
  - Nach dem Wandern einer Einheit auf dem orangen Stab (Foto 2) ist es oben und unten umgekehrt.
  - Dann waeren die Ecken Quellen und Senken, keine reinen Durchgangsstellen. Ob die Anordnung so gemeint ist, muss Finn
    sagen.

## 3. Was folgt [H]

1. **Fuer echte Kraefte (Lesart A)** traegt ein einzelnes Knicklicht-Tetraeder keinen Kraftfluss, nur Biegung. Fluss
   entsteht mit aeusserer Last oder durch Verspannung beim Zusammensetzen. Wie weit er dann in einem Netz reicht,
   entscheidet die Steifigkeit: Im steifen Netz wird abgeschirmt, im gerade-noch-starren Netz koennte er weit tragen.
   Das ist Teil 2 und 3 von EIS-1.
2. **Fuer erhaltene Einheiten (Lesart B)** ergibt ein grosses Tetraedernetz mit "so viel rein wie raus" an jeder Ecke
   Coulomb-artige Fernkraefte zwischen Quellen und Senken.
   - Das gilt fuer "entlang der Kanten" wie fuer "durch die Tetraeder"; entscheidend ist die Erhaltung, nicht der Weg.
   - Ein einzelnes Tetraeder hat dafuer zu wenig Platz; es braucht ein Netz.
3. **Fuer Schwerkraft** muessten die Einheiten Tensorgroessen tragen (Kraft und Richtung zusammen, wie die Spannung im
   Festkoerper). Das fuehrt zu den Fraktonen und zur Dualitaet Elastizitaet <-> Tensor-Eichtheorie [L: Pretko und
   Radzihovsky 2018].

## 4. Vorschlag: FLUSS-1 (kleiner Test, nach Finns Antwort)

- Erhaltene Einheiten auf den Kanten eines grossen Pyrochlor-Netzes (Tetraederkanten, "entlang").
  - Ganzzahliger Fluss je Kante, Kirchhoff an jeder Ecke, Gewicht exp(-sum Fluss^2 / T).
  - Eine Quelle und eine Senke im Abstand r.
- **Vorhersage:** Die freie Energie folgt a - C/r (Coulomb), wie im Spin-Eis "durch die Tetraeder" (EIS-1, Teil 1).
- **Gegenprobe:** Mit Kosten auf dem Fluss der ganzen Tetraederflaeche statt der Kante sollte dasselbe herauskommen.
- Das zeigt, dass Erhaltung, nicht Geometrie, die Fernkraft macht.
