# Wellen 20 (Zufallskarte): Geknotete Q-Baelle, nur Papier und Literatur

Bearbeiter: Anthropic-Agent (Opus 5.5) fuer claude-primary, Runde 3. Datei begonnen 2026-09-30 01:57:18 CEST (gemessen).
Explorativ. Eigene Schreibtischargumente sind mit **[S]** markiert, Hausbelege mit **[Haus]**, Gelesenes mit **[L]**,
Suchtreffer ohne Lektuere mit **[T]**. Nichts ist gerechnet.

## Ergebnis

1. **Ein-Feld-Modell (Ziel C): keine geknoteten Q-Baelle als stabile Objekte.**
   - Es gibt keine Knotenzahl. Die Hopfzahl lebt in pi_3(S^2) = Z. Unser Feld nimmt Werte in C an, und jede
     Abbildung S^3 -> C ist zusammenziehbar **[S]**. Der Konfigurationsraum H^1(R^3, C) ist konvex, also
     zusammenziehbar; das ist derselbe Befund wie beim Spin-1/2-Entscheid vom 23.09. **[Haus]**.
   - Geknotet sein koennen nur die Nullinien von psi (Wirbellinien), etwa als Wirbelknoten im Innern eines grossen
     Q-Balls. Ihr Knotentyp ist aber nicht erhalten: Wo sich zwei Nullinien treffen, koennen sie sich mit endlicher
     Energie umverbinden **[S]**.
   - Genau das zeigt die Superfluid-Literatur: In der Gross-Pitaevskii-Gleichung entknoten sich 322 untersuchte Knoten
     und Verschlingungen ausnahmslos durch Umverbindungen **[T, Abstract-Aussage]** (Kleckner, Kauffman, Irvine, Nat. Phys. 12, 650
     (2016)). Das Innere eines duennwandigen Q-Balls ist ein dichtes Kondensat mit positiver Schallgeschwindigkeit
     (c_s^2 = S U''/(S U'' + 2 omega^2), etwa 0,5 bei S = 1 **[S]**). Es verhaelt sich also wie ein solches Superfluid.
   - **Hypothese [S]:** Ein Wirbelknoten in einem grossen Q-Ball entknotet sich wie im Superfluid. Ein Knoten waere hoechstens
     ein Uebergangszustand.
   - Bekannt sind im Ein-Feld-Sektor drehende Q-Baelle mit Wirbelachse (J = m Q) und Wirbelringe ("Q-rings", als
     semitopologisch und metastabil beschrieben). Beides steht in der Uebersicht von Radu und Volkov (Phys. Rep. 468,
     101 (2008), arXiv:0804.1357, Abstract gelesen **[L]**), mit ihren "twisted" Verallgemeinerungen.
   - Einen stationaeren geknoteten Q-Ball mit einem einzigen komplexen Skalarfeld habe ich nicht gefunden. Gesucht
     habe ich mit zwei Anfragen, also nicht gruendlich.
2. **Erweitertes Modell C x S^2: geknotete, isorotierende Solitonen sind Literatur. Ob ein gebundener "Knoten-Q-Ball"
   aus altem Q-Ball und Hopfion existiert, ist offen und haengt an einem Frequenzfenster.**
   - Das S^2-Feld n traegt die Hopfzahl h. Mit Faddeev-Skyrme-Term (Derrick-Stabilisierung) gibt es stabile Knoten:
     Faddeev und Niemi, Nature 387, 58 (1997) **[T]**; Battye und Sutcliffe 1998/1999 **[Haus]** (die VK-Konstante
     ist dort gegen Battye-Sutcliffe 1999 und Sutcliffe 2007 nachgerechnet).
   - Die isorotierenden Knoten sind "topologische Q-Baelle".
     - Harland, Jaeykkae, Shnir und Speight, J. Phys. A 46, 225402 (2013), arXiv:1301.2923 **[L]**: Die Form haengt
       nicht von omega ab; die Groesse waechst monoton mit omega.
     - Die Pseudoenergie F_omega ist nur fuer omega < min{1, mu} (ihre Einheiten) nach unten beschraenkt. Oberhalb von
       mu strahlen die Solitonen Mesonen ab. Fuer mu > 1 kollabieren sie in der Regel schon vorher, wegen der
       Geschwindigkeitsabhaengigkeit des Skyrme-Terms (Abschnitte 2 und 3.2 **[L]**).
     - "Hopf Q-balls" als exakte stationaere Hopfionen im CP^1-Modell mit Potential: Sanchez-Guillen, Adam und
       Wereszczynski, Eur. Phys. J. C 47, 513 (2006), hep-th/0602008 **[L]**.
   - **In unserem C x S^2 [Haus]:**
     - Die Frequenzschranke steht in literatur-20260924/CXS2-TORE-astra-20260924.md, Gleichung F1: Hinreichend ist
       omega^2 < v^2/(2 kappa).
     - Der CX-1-Autor hat hergeleitet, dass jeder isorotierende Hopftraeger mit h ungleich 0 oberhalb dieser Grenze bei
       fester Ladung unendlich viele negative Richtungen hat. Das deckt sich mit Harland u. a.; ein anderes Haus hat es
       nicht nachgerechnet (ARBEITSFELD, CX-1-Eintrag C1).
   - **Folge fuer den Knoten-Q-Ball [S aus Haus-Bausteinen]:**
     - Ein gebundener Zustand aus altem Q-Ball (Feld phi) und Hopfion (Feld n) mit gemeinsamer Frequenz braucht
       1/2 < omega^2 < min(1, v^2/(2 kappa)). Die gemeinsame Frequenz kommt von der Paarkopplung G, denn dann bleibt
       nur eine U(1)-Ladung erhalten (Gleichungen L2 und L3 im Torpapier).
     - Am urspruenglichen Skelett (v = mu = kappa = 1) ist v^2/(2 kappa) = 1/2. Das Fenster ist dann leer, beide
       Bedingungen beruehren sich nur.
     - CX-1 hat deshalb kappa = 1/4 gewaehlt (Parameterpunkt P*, CX-1-Eintrag C4). Dort ist das Fenster
       1/2 < omega^2 < 1 offen.
   - **Stand:**
     - CX-1 ist ein reiner Qualifikationsvertrag fuer die beiden Referenzaeste (Tor T2) und wartet auf das
       Ollama-Pausenfenster.
     - Der gemischte Ast (Tor T4) ist weder definiert noch gerechnet.
     - Die Machbarkeitsrechnung fand fuer reines Faddeev-Skyrme mit h = 1: E_norm = 1,2226 gegen etwa 1,21 in der
       Literatur, Hopfzahl 0,9995. Ein zu grobes Gitter liess den Knoten kollabieren; daraus wurden die Gitter dx = 1/18
       und 1/12 **[Haus]**.
3. **Messbezug nur fremd:** Knotensolitonen wurden in einem Spinor-Kondensat (mehrkomponentig, S^2-artiger Ordnungsparameter)
   erzeugt, "Tying quantum knots", Nat. Phys. (2016) **[T, Inhalt aus dem Gedaechtnis]**. Das betrifft den C x S^2-Typ, nicht unseren Ein-Feld-Q-Ball und
   keine Q-Ball-Daten.

## Kurzbegruendung der Topologie [S]

- Ein-Feld: Endliche Energie heisst psi -> 0 im Unendlichen, also eine Abbildung S^3 -> C. Weil C zusammenziehbar ist,
  gibt es keine Homotopieklassen. Die Phase psi/|psi| ist nur ausserhalb der Nullmenge definiert; ihr Windungsinhalt
  sitzt auf den Nullinien. Deren Verknuepfung ist unter stetiger Deformation mit Durchgang durch psi = 0 nicht erhalten.
- C x S^2: Ist n = Nordpol im Unendlichen vorgeschrieben (Potential mu^2 v^2 (1 - n3)), dann ist n eine Abbildung
  S^3 -> S^2, und die Hopfzahl h in pi_3(S^2) = Z bleibt unter endlicher Energie erhalten. Den Kollaps verhindert erst der
  Vierableitungsterm kappa (Derrick); ohne ihn schrumpft der Knoten.
- Der Faktor C (Feld phi) traegt nichts zur Knotenzahl bei. Der "Knoten" eines Knoten-Q-Balls sitzt immer im n-Feld.
  phi bringt Ladung und Bindung.

## Was offen bleibt (Vorschlag, nicht Teil dieser Karte)

- **Ein-Feld (3D, klein, L4-nah):** Wie lange lebt ein Kleeblattknoten der Nullinie in einem grossen Q-Ball
  (omega^2 = 0,52) bis zur ersten Umverbindung, abhaengig vom Ballradius? Erwartung: kurz, etwa einige Umlaufzeiten
  des Wirbels. Das waere nur die GP-Aussage im Tropfen.
- **C x S^2:** Die eigentliche Frage ist die Bindung des gemischten Astes im Fenster 1/2 < omega^2 < 1 bei kappa = 1/4.
  Sie gehoert zum CX-1-Strang (Tor T4) und braucht keine neue Karte.

## Latten

| Latte | Einschaetzung |
|---|---|
| L1 kann scheitern | ja: Ein-Feld scheitert, wenn ein langlebiger Knoten gefunden wird. C x S^2 scheitert, wenn das Fenster bei P* trotz F1 leer ist oder der gemischte Ast nicht existiert |
| L2 Gegenprobe | teilweise: Topologie (pi_3(C) = 0 gegen pi_3(S^2) = Z); Literaturkontrollen GP (Knoten entknoten sich) und Faddeev-Skyrme (Hopfionen stabil) |
| L3 Numerik | entfaellt (Papier); fuer C x S^2 liegt die Numerik bei CX-1 (Machbarkeit E_norm 1,2226, Hopfzahl 0,9995) |
| L4 schon bekannt | ja: Hopfionen, isorotierende Hopfionen samt Frequenzgrenze, Entknoten in GP |
| L5 Messbezug | nein fuer unser Modell; fremd: Knoten in Spinor-Kondensaten |

**Vorschlag:**
- Ein-Feld-"Knoten-Q-Ball": verwerfen (keine Knotenzahl; bekannt).
- C x S^2: parken beim CX-1-Strang. Die Karte liefert dafuer nur die Fensterbedingung 1/2 < omega^2 < min(1, v^2/(2 kappa)).

## Quellen

- Kleckner, Kauffman, Irvine, How superfluid vortex knots untie, Nat. Phys. 12, 650 (2016),
  https://www.nature.com/articles/nphys3679 (Abstract-Aussage aus dem Suchtreffer; Volltext nicht gelesen)
- Harland, Jaeykkae, Shnir, Speight, Isospinning hopfions, J. Phys. A 46, 225402 (2013), https://arxiv.org/abs/1301.2923
  (Abstract und Abschnitte 2 und 3.2 ueber die HTML-Fassung)
- Radu, Volkov, Stationary ring solitons in field theory - knots and vortons, Phys. Rep. 468, 101 (2008),
  https://arxiv.org/abs/0804.1357 (Abstract)
- Sanchez-Guillen, Adam, Wereszczynski, Hopf solitons and Hopf Q-balls on S^3, Eur. Phys. J. C 47, 513 (2006),
  https://arxiv.org/abs/hep-th/0602008 (Abstract)
- Faddeev, Niemi, Stable knot-like structures in classical field theory, Nature 387, 58 (1997),
  https://www.nature.com/articles/387058a0 (nur Suchtreffer)
- Tying quantum knots, Nat. Phys. (2016), https://www.nature.com/articles/nphys3624 (nur Suchtreffer)
- Weitere Suchtreffer, nicht gelesen: Semitopological Q-Rings (hep-ph/0111354), Q-vortices, Q-walls and coupled Q-balls
  (arXiv:1101.5366), Torus knots as Hopfions (arXiv:1304.6021), Massive Hopfions (arXiv:1012.2595)
- Hausbelege: literatur-20260924/CXS2-TORE-astra-20260924.md (L1-L3, F1); ARBEITSFELD-claude-primary.md, CX-1-Eintraege
  C1 bis C4 und "CX-1 Fassung 2"; Gedaechtnis "Spin 1/2: unveraenderte Formel kann es nicht" (23.09.)

## Einfach gesagt

Ein echter Knoten braucht etwas, das ihn festhaelt. In unserem Ein-Feld-Modell fehlt das: Man kann einen Knoten
hineinbauen, aber er kann sich wie ein Wirbelknoten im Superfluid von selbst loesen, und genau das beobachten Rechnungen
an Superfluiden. Im erweiterten Modell mit der "Kompassnadel" an jedem Punkt gibt es dagegen eine echte Knotenzahl.
Dort sind drehende Knoten aus der Fachliteratur bekannt, allerdings nur bis zu einer Hoechstdrehzahl. Ob unser alter
Q-Ball und so ein Knoten zusammen ein gebundenes Paket bilden, ist offen. Moeglich ist es nur in einem schmalen
Drehzahlfenster, und das prueft der schon vorbereitete Rechenvertrag CX-1.

Ende der Bearbeitung dieser Karte: siehe PLAN.md, letzte Zeile.
